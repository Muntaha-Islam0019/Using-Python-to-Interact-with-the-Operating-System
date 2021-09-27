# while loop example

"When using while loops and bash scripts, it's common to have a loop that retries a command a number of times until it succeeds. This is really useful with commands that use network connections or that access resources that might be locked. These commands can fail for external reasons and they're likely to succeed after a retry or two."

# its not my clumsiness, instead, we need to put no space on assigning value to variables in bash
n=0

"we're getting the value of a command line argument using the $1. In Python, we get the same information using sys.argv[1]"
command=$1

"until either the command succeeds or the end variable reaches a value of five"
while ! $command && [ $n -le 5 ]; do

    "This is no time for rest, the idea here is that if the command we're calling is failing due to CPU usage, network or resource exhaustion, it might make sense to wait a bit before trying again."
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;