package main

import (
	"fmt"
	"runtime"
)

func ExecutePipeline(hashSignJobs ...job) {
	in := make(chan interface{}) //
	var wgexec sync.WaitGroup

	for _, Job := range hashSignJobs {
		out := make(chan interface{})

		wgexec.Add(1)
		go Worker(&wgexec, Job, in, out)
		in = out
		fmt.Println("------------>", runtime.NumGoroutine())
	}
	fmt.Println(wgexec, "+++++")
	wgexec.Wait()
}

func Worker(wgexec *sync.WaitGroup, Job job, in, out chan interface{}) {
	defer wgexec.Done()
	defer close(out)
	Job(in, out)

}

func SingleHash(in, out chan interface{}) {
	var wg sync.WaitGroup
	for val := range in {
		fmt.Println("---->", val)
		data := fmt.Sprintf("%v", val)
		crcMd5 := DataSignerMd5(data)
		wg.Add(1)
		go SingleHashJob(&wg, data, crcMd5, out)
	}
	wg.Wait()
}

func SingleHashJob(wg *sync.WaitGroup, data string, md5 string, out chan interface{}) {
	defer wg.Done()
	fmt.Println("shj", data)
	res := DataSignerCrc32(data) + "~" + DataSignerCrc32(md5)
	out <- res

}

func MultiHash(in, out chan interface{}) {
	var wgm sync.WaitGroup
	for v := range in {
		str, ok := v.(string)
		if !ok {
			return
		}
		wgm.Add(1)
		go MultiHashJob(&wgm, out, str)
	}
	wgm.Wait()
}

func MultiHashJob(wgm *sync.WaitGroup, out chan interface{}, value string) {
	defer wgm.Done()
	arr := make([]string, 6)
	for i := 0; i < 6; i++ {
		fmt.Println("mhj", value)
		v := DataSignerCrc32(strconv.Itoa(i) + value)
		arr = append(arr, v)
	}
	result := ""
	for _, v := range arr {
		result = result + v
	}
	out <- result

}

func CombineResults(in, out chan interface{}) {
	var arr []string
	for v := range in {
		str, ok := v.(string)
		if !ok {
			return
		}

		arr = append(arr, str)
		fmt.Println("com", arr)
		fmt.Println("======>", runtime.NumGoroutine())
	}
	result := strings.Join(arr, "_")
	fmt.Println(result)
	out <- result
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
		job(MultiHash),
		job(CombineResults),
		job(func(in, out chan interface{}) {
			fmt.Println("=-=-=-=-=-=", runtime.NumGoroutine())
			for v := range in {
				dataRaw := v
				data, ok := dataRaw.(string)
				if !ok {
					fmt.Println("cant convert result data to string")
				}
				fmt.Println("*", data)
			}
		}),
	}

	ExecutePipeline(hashSignJobs...)
	fmt.Println("======>", runtime.NumGoroutine())

}
