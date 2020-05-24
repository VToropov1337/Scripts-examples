package main

func SingleHash(strs ...string) <-chan interface{} {
	out := make(chan interface{})
	go func() {
		for _, v := range strs {
			out <- v
		}
		close(out)
	}()

	return out

}

func SingleHashJob(in <-chan interface{}) <-chan interface{} {
	out := make(chan interface{})
	go func() {
		for v := range in {
			str, ok := v.(string)
			if !ok {
				return
			}
			res := DataSignerCrc32(str) + "~" + DataSignerCrc32(DataSignerMd5(str))
			out <- res
		}
		close(out)
	}()
	return out

}

func MultiHash(in <-chan interface{}) <-chan interface{} {
	out := make(chan interface{})
	go func() {
		for v := range in {
			str, ok := v.(string)
			if !ok {
				return
			}
			res := MultiHashJob(str)

			out <- res
		}
		close(out)
	}()

	return out

}

func MultiHashJob(v string) string {
	arr := make([]string, 6)
	for i := 0; i < 6; i++ {
		v := DataSignerCrc32(strconv.Itoa(i) + v)
		arr = append(arr, v)
	}
	result := ""
	for _, v := range arr {
		result = result + v
	}
	// out <- result
	return result

}

func CombineResults(in <-chan interface{}) string {
	result := ""
	var arr []string

	for v := range in {
		str, ok := v.(string)
		if !ok {
			return ""
		}
		arr = append(arr, str)
	}
	result = strings.Join(arr, "_")

	return result
}

func main() {
	arr := []string{"0", "1"}
	a := SingleHash(arr...)
	b := SingleHashJob(a)
	c := MultiHash(b)
	d := CombineResults(c)
	fmt.Println(d)
}
