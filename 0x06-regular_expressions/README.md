![Holberton](https://user-images.githubusercontent.com/85451781/140782830-f3f4a341-3d98-4a6e-89d2-76d684c80e9e.png)

# 0x06. Regular expression

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```bash
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Tasks

### 0. Simply matching School

Requirements:

- The regular expression must match School
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```bash
sylvain@ubuntu$ ./0-simply_match_holberton.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 0-simply_match_school.rb

### 1. Repetition Token #0

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
  **Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 1-repetition_token_0.rb

### 2. Repetition Token #1

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 2-repetition_token_1.rb

### 3. Repetition Token #2

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
  **Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 3-repetition_token_2.rb

### 4. Repetition Token #3

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets
  **Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 4-repetition_token_3.rb

### 5. Not quite HBTN yet

Requirements:

- The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 5-beginning_and_end.rb

### 6. Call me maybe

This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.

Requirement:

- The regular expression must match a 10 digit phone number

Example:

```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 6-phone_number.rb

### 7. OMG WHY ARE YOU SHOUTING?

Requirement:

- The regular expression must be only matching: capital letters

Example:

```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x06-regular_expressions
- File: 7-OMG_WHY_ARE_YOU_SHOUTING.rb
