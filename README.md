# Sebastian...
is a discord bot uses Gemini 1.0-Pro (provide your own API key)
Along with the discord api token.
This build currently runs on Linux (Windows is experimental, will have to test for that...)

Add the bot to your discord server and type !read "https://archlinux.org/" It will scrape the webpage and recurse into a few hyper links
(you can adjust the optional function arguments to change this default value if you want it to scrape more data, rather than just from
the webpage supplied. However this could result in an ERROR due to the file being extremely large for the free version of gemini.)

converts HTML to Markdown and output gets piped to the gemini model and you can then ask it questions about the website.

Commands: !help - Displays this message !read https://website1.com https://website2.com, etc... - Reads websites seperated by spaces !talk - Starts a conversation with me !stop - Stops the conversation and clears the websites read
