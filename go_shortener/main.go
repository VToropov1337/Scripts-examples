package main

import (
	"fmt"
	"go_shortener/urlshort"
	"net/http"
)

func main() {
	mux := defaultMux()
	pathsToUrls := map[string]string{
		"/reflect": "https://golang.org/pkg/reflect/",
		"/yaml-godoc":     "https://godoc.org/gopkg.in/yaml.v2",
	}
	mapHandler := urlshort.MapHandler(pathsToUrls, mux)

	yaml := `
- path: /urlshort
  url: https://golang.org/pkg/image/color/
- path: /urlshort-final
  url: https://github.com/boltdb/bolt
`
	yamlHandler, err := urlshort.YAMLHandler([]byte(yaml), mapHandler)
	if err != nil {
		panic(err)
	}
	fmt.Println("Starting the server on :8080")
	http.ListenAndServe(":8080", yamlHandler)
}

func defaultMux() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/", hello)
	return mux
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello, world!")
}

