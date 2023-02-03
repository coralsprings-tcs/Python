# Programming - absolute basics

A program makes a computer usable. Without a program, a computer, even the most powerful one, is nothing more than an object.

Contemporary computers can only evaluate the results of very fundamental operations, like adding or dividing, but they can do it very fast, and can repeat these actions virtually any number of times.

Imagine that you want to know the average speed you've reached during a long journey. You know the distance, you know the time, you need the speed. Naturally, the computer will be able to compute this, but the computer is not aware of such things as distance, speed, or time. Therefore, it is necessary to instruct the computer to:
* accept a number representing the distance;
* accept a number representing the travel time;
* divide the former value by the latter and store the result in the memory;
* display the result (representing the average speed) in a readable format.
These four simple actions form a program. Of course, these examples are not formalized, and they are very far from what the computer can understand, but they are good enough to be translated into a language the computer can accept.

## Natural languages vs. programming languages
A language is a means (and a tool) for expressing and recording thoughts such as Greek, English, Sumerian, etc. Some of them require neither speaking nor writing, such as body language.

Computers have their own language, too, called machine language, which is very rudimentary. The commands it recognizes are very simple. We can imagine that the computer responds to orders like "take that number, divide by another and save the result".

A complete set of known commands is called an instruction list, sometimes abbreviated to IL. Different types of computers may vary depending on the size of their ILs, and the instructions could be completely different in different models.

Note: machine languages are developed by humans.

No computer is currently capable of creating a new language. However, that may change soon. Just as people use a number of very different languages, machines have many different languages, too. The difference, though, is that human languages developed naturally.

Moreover, they are still evolving, and new words are created every day as old words disappear. These languages are called natural languages.

### What makes a language?
We can say that each language (machine or natural, it doesn't matter) consists of the following elements:
* an alphabet: a set of symbols used to build words of a certain language (e.g., the Latin alphabet for English, the Cyrillic alphabet for Russian, Kanji for Japanese, and so on)
* a lexis: (aka a dictionary) a set of words the language offers its users (e.g., the word "computer" comes from the English language dictionary, while "cmoptrue" doesn't; the word "chat" is present both in English and French dictionaries, but their meanings are different)
* a syntax: a set of rules (formal or informal, written or felt intuitively) used to determine if a certain string of words forms a valid sentence (e.g., "I am a python" is a syntactically correct phrase, while "I a python am" isn't)
* semantics: a set of rules determining if a certain phrase makes sense (e.g., "I ate a doughnut" makes sense, but "A doughnut ate me" doesn't)
The IL is, in fact, the alphabet of a machine language. This is the simplest and most primary set of symbols we can use to give commands to a computer. It's the computer's mother tongue.

### Where programming languages come in
We need a language in which humans can write their programs and a language that computers may use to execute the programs, one that is far more complex than machine language and yet far simpler than natural language.

Such languages are often called high-level programming languages. They are at least somewhat similar to natural ones in that they use symbols, words and conventions readable to humans. These languages enable humans to express commands to computers that are much more complex than those offered by ILs.

A program written in a high-level programming language is called a source code (in contrast to the machine code executed by computers). Similarly, the file containing the source code is called the source file.

High-level is different from low-level languages, such as Rust, C++, HolyC, etc. and this will be discussed in Compilation vs. Interpretation
