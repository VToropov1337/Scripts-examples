package main

import (
	"fmt"
	"runtime"
)

func ExecutePipeline(hashSignJobs ...job) {
	in := make(chan interface{}) //
	for _, Job := range hashSignJobs {
		out := make(chan interface{})
		go Worker(Job, in, out)
		in = out
		fmt.Println("------------>", runtime.NumGoroutine())
	}
}

func Worker(Job job, in, out chan interface{}) {
	Job(in, out)

}

func SingleHash(in, out chan interface{}) {

	for val := range in {
		fmt.Println("---->", val)
		data := fmt.Sprintf("%v", val)
		crcMd5 := DataSignerMd5(data)
		go SingleHashJob(data, crcMd5, out)
	}
}

func SingleHashJob(data string, md5 string, out chan interface{}) {

	res := DataSignerCrc32(data) + "~" + DataSignerCrc32(md5)
	out <- res

}

func main() {
	inputData := []string{"0", "1"}
	hashSignJobs := []job{
		job(func(in, out chan interface{}) {
			for _, fibNum := range inputData {
				out <- fibNum
			}
		}),
		job(SingleHash),
		job(func(in, out chan interface{}) {
			for v := range in {
				dataRaw := v
				data, ok := dataRaw.(string)
				if !ok {
					fmt.Println("cant convert result data to string")
				}
				fmt.Println(data)

			}
			// dataRaw := <-in
			// data, ok := dataRaw.(string)
			// if !ok {
			// 	fmt.Println("cant convert result data to string")
			// }
			// fmt.Println(data)
		}),
	}
	ExecutePipeline(hashSignJobs...)
	fmt.Scanln()

}
