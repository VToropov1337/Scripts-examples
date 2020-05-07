package main

import (
	"encoding/xml"
	"io/ioutil"
	"log"
	"net/http"
	"sync"
	"text/template"
)

var wg sync.WaitGroup

type NewsAggPage struct {
	Title string
	News  map[string]NewsMap
}

type NewsMap struct {
	Title string
	Data  string
}

type News struct {
	Urls     []string `xml:"url>loc"`
	Titles   []string `xml:"url>news>title"`
	PubDates []string `xml:"url>news>publication_date"`
}

func newsRoutine(c chan News, Location string) {
	defer wg.Done()
	var n News
	resp, _ := http.Get(Location)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &n)
	resp.Body.Close()
	c <- n

}
func newsAggHandler(w http.ResponseWriter, r *http.Request) {

	SitemapIndex := []string{"https://www.washingtonpost.com/news-politics-sitemap.xml",
		"https://www.washingtonpost.com/news-opinions-sitemap.xml",
		"https://www.washingtonpost.com/news-national-sitemap.xml",
		"https://www.washingtonpost.com/news-technology-sitemap.xml",
		"https://www.washingtonpost.com/news-sports-sitemap.xml",
		"https://www.washingtonpost.com/news-local-sitemap.xml",
		"https://www.washingtonpost.com/news-business-sitemap.xml",
		"https://www.washingtonpost.com/news-lifestyle-sitemap.xml",
		"https://www.washingtonpost.com/news-entertainment-sitemap.xml"}

	news_map := make(map[string]NewsMap)

	queue := make(chan News, 10)
	for _, Location := range SitemapIndex {
		wg.Add(1)
		go newsRoutine(queue, Location)
	}
	wg.Wait()
	close(queue)

	for element := range queue {
		for idx, _ := range element.Titles {
			news_map[element.Urls[idx]] = NewsMap{element.Titles[idx], element.PubDates[idx]}
		}
	}

	p := NewsAggPage{Title: "Summary", News: news_map}
	t, _ := template.ParseFiles("basic.html")
	t.Execute(w, p)
}

func main() {
	http.HandleFunc("/", newsAggHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
