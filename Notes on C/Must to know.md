
# Function prototypes

It is a function declaration without a body before `main()` and it ensures that function invocations are made with the correct arguments.

## Utility

- Many C compilers do not check for parameter matching.
- Missing arguments will result in unexpected behavior.
- A function prototype causes the compiler to flag an error if arguments are missing.

**Example:**

```C
int fib(int n); // <==== Function Prototype 

int main(){
	result = fib("a"); // <====== Bad argument 
	printf("%d", result);
}

int fib(int n){
	if (n <= 1){
		return 1;
	}
	else{
		return fib(n-1) + fib(n-2);
	}
}

```

output:
```bash
error: passing argument 1 of ‘fib’ makes integer from pointer without a cast.

  15 |     printf("result: %d", fib("a"));
      |                              ^~~
      |                              |
      |                              char *
functions.c:4:13: note: expected ‘int’ but argument is of type ‘char *’
    4 | int fib(int n){
      |         ~~~~^

```