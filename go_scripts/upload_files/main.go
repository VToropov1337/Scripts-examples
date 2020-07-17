package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"net/http"
)

var tpl = template.Must(template.ParseFiles("index.html"))
var scs = template.Must(template.ParseFiles("success.html"))

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.Execute(w, nil)
}

func uploadFile(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "Uploading file\n")

	// Parse our multipart form, 10 << 20 specifies a maximum
	// upload of 10 MB files.
	r.ParseMultipartForm(10 << 20)
	// FormFile returns the first file for the given key `myFile`
	// it also returns the FileHeader so we can get the Filename,
	// the Header and the size of the file
	file, handler, err := r.FormFile("myFile")
	if err != nil {
		fmt.Fprintf(w, "Error Retrieving the File")
		fmt.Println(err)
		return
	}
	defer file.Close()
	fmt.Printf("Uploaded File: %+v\n", handler.Filename)
	fmt.Printf("File Size: %+v\n", handler.Size)
	fmt.Printf("MIME Header: %+v\n", handler.Header)

	tempFile, err := ioutil.TempFile("temp-images", "upload-*.png")
	if err != nil {
		fmt.Println(err)
	}
	defer tempFile.Close()

	fileBytes, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println(err)
	}

	tempFile.Write(fileBytes)

	// fmt.Fprintf(w, "Successfully Uploaded File\n")
	// http.Redirect(w, r, "/", 302)
	scs.Execute(w, "success.html")
}

func setupRoutes() {
	http.HandleFunc("/upload", uploadFile)
	http.HandleFunc("/", IndexHandler)
	http.ListenAndServe(":8080", nil)
}

func main() {
	setupRoutes()
}
