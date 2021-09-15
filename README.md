## COS 460/540 - Computer Networks
# Project 1: Number Guessing Server

## Specification
Your goal is to develop a TCP/IP based server that implements a number guessing
game. This assignment is an introduction to TCP/IP socket programming and
connecting clients and servers together. You will only be responsible for the
server side of things, you can use “telnet” for testing and validation.
Additionally you can use telnet, a simple text-based client to interact with
your server.

## The Game
The game is to guess a number between 1 and 100. After a client connects, the
server will silently choose a random number and give higher/lower hints to the
player as they try to guess the chosen number.

## The Protocol
The server should be listening and accepting connections from clients. Upon
connection, the server will send a welcome message, one line with the plus
symbol (`+`) as the first character , and then await the client's first guess,
again one line. After each guess the server should respond with the greater than
(`>`) or less than symbol (`<`) as the first character on the line to reflect
`higher` or `lower` and then accept another guess. If the guess is correct, the
server should respond with an asterisk (`*`) as the first character on a single
congratulatory message line and disconnect the connection.

### Example
The following is an example interaction with the server. User entered text is in
bold font. System or server generated responses are in normal font. Pay special
attention to the first character of each line from the server and the whitespace
that immediately follow it. These are the key elements of the Protocol that must
be followed.

```
$ telnet localhost 1029
+ Hello. I’m thinking of a number between 1 and 100. Can you guess it?
50
< My number is lower.
25
> Higher.
Go go gadget guesser!
! Invalid input, please enter only numbers between 1 and 100.
35
> Higher.
42
* That’s it. Good job. It took you 3 guesses. Thanks for playing.
$
```

### Protocol Specification
The following is the detailed protocol specification using the IETF Augmented
BNF Syntax from RFC 2234.

```
; For definitions of CRLF, DIGIT, WSP, VCHAR see RFC 2234
; TEXT is any arbitrary whitespace and printable characters
TEXT	= *(WSP / VCHAR)

; The client session consists of a series of guesses until
; the connection is closed by the server. Each guess is a
; sequence of DIGITS followed by a CRLF.
client-session 	= *(guess)

guess	= *DIGIT CRLF

; The server session consists is a hello and correct
; that bracket a series of lower, higher, and invalid
; responses to client guesses. Each response is terminated
; with a CRLF. The server closes the connection after the
; CRLF that follows the correct response.
server-session 	= hello CRLF 
guess-response CRLF
correct CRLF 
; connection terminates

guess-response	= ( lower / higher / invalid ) CRLF
			
; Hello message, on initial connection only
hello		= “+” WSP TEXT

; Guess was too high
lower		= “<” WSP TEXT

; Guess was too low
higher		= “>” WSP TEXT

; Guess was invalid (out of range or non-numeric, non-parsable)
invalid		= “!” WSP TEXT

; Guess was the correct number
correct		= “*” WSP TEXT
```

## Additional Information
* The server must accept as a configurable parameter (on the command line) the port number to listen on.
* You must include the file named PLAYBOOK.md
* PLAYBOOK.md has <<Your name>>
* PLAYBOOK.md has what language you used
* PLAYBOOK.md has a brief synopsis of your experience with the assignment (1-3 paragraphs).
* PLAYBOOK.md has how to compile and execute your project.
* You must not include any executable binary files. Submit only code.
* You may include a script or batch file to compile and/or run your server. This must be documented in your PLAYBOOK.md if it is included.
* You must submit your project through [GitHub](http://github.com)

## Definitions
The IETF Best Practice Document RFC 2119 Key words for use in RFCs to Indicate
Requirement Levels defines several keywords that are used in this assignment and
throughout the course. Pay special attention to where they appear in the
assignment.

Some keywords used in this assignment are as follows;

**MUST**: This word, or the terms **REQUIRED** or **SHALL**, mean that the
definition is an absolute requirement of the specification.

**SHOULD**: This word, or the adjective **RECOMMENDED**, mean that there may
exist valid reasons in particular circumstances to ignore a particular item, but
the full implications must be under.

**MAY**: This word, or the adjective **OPTIONAL**, mean that an item is truly
optional. One vendor may choose to include the item because a particular
marketplace requires it or because the vendor feels that it enhances the product
while another vendor may omit the same item.
