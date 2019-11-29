# Go (golang) Lessons Learned

## 2015
### Day 1
* If you call `log.Fatal` any `defer` statements in your program will not be executed because `log.Fatal` calls `os.Exit`
which terminates the program immediately. In this specific case where you want the `defer` statements to always run even
when an error occurs `log.Panic` is a good choice because it unwinds the program and executes the `defer` statements.
  
## 2018
### Day 1
* The `int` datatype in Go can change based upon the platform they run on so it's important to be explicit (declare variables as `int64` instead of `int`).
