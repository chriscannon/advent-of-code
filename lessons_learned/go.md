# Go (golang) Lessons Learned

## 2015
### Day 1
* If you call `log.Fatal` any `defer` statements in your program will not be executed because `log.Fatal` calls `os.Exit`
which terminates the program immediately. In this specific case where you want the `defer` statements to always run even
when an error occurs `log.Panic` is a good choice because it unwinds the program and executes the `defer` statements.
  
## 2018
### Day 1
* The `int` datatype in Go can change based upon the platform they run on so it's important to be explicit (declare variables as `int64` instead of `int`).

## 2019
### Day 1
* By default go's `/` operator does floor division.

### Day 2
* To start a go module run `go mod init <MODULE_NAME>`.
* Go does not check for overflow (e.g., uint's can overflow) so be careful.
* Use the built-in `copy` command to copy slices.
* To break a for loop inside a switch use a label like so:
```go
loop:
for i := range input {
    switch i {
    default:
        break loop
    }
}
```
* To set a custom split character on a `scanner` create a `bufio.SplitFunc` and set it using `scanner.Split()`.

### Day 3
* Golang has no absolute function for ints. You have to write your own like this:
```go
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
```
* If you want to store multiple values as a key in a map you have to first create a struct which holds those values and
then set that new struct as the key.

### Day 4
* To reference a capture group *inside* a regular expression you can use `\NUM_CAPTURE_GROUP` where the number corresponds
to the position of the capture group. For example, if you wanted to match two digits that are the same your regular expression
would look like `(\d)\1` which says capture any digit and then match that same digit you captured on next to it.
* If you want to iterate over the digits of any number instead of casting to a string and iterating each character you can do 
so with division and modulus like so:
```go
num := 123456789
n := 9 // the length of num
for i := n - 1; i >= 0; i-- {
	denominator := int(math.Pow(10, float64(i)))
	digit := (num/denominator)%10
}
```

### Day 6
* If you need to work your way from the leaf of a tree to the root build the tree in reverse and do a depth-first search.
* To find the parent of two leaf nodes build a reverse tree, get the path from each leaf to the root, then traverse each path
until you find a common node ID which is the common parent of both leaf nodes.

### Day 7
* Buffered channels are a good way to ensure that go routines using a channel do not have to be in exact lock step
for reads/writes. Using a buffered channel of size 1 is a good place to start.