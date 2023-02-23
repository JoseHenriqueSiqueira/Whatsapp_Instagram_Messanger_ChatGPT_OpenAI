## class MessengerBotGPT:
### def __init\__(user, chatbot):
Initializes the ChromeDriverManager service, creates a webdriver. Chrome instance, and navigates to the chat page of the provided Messenger username.
| Parameter   | type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user`| `string` | **Mandatory**. The Messenger username target to start a chat|
| `chatbot`| `object` | **Mandatory**. Instance of the ChatBot class.|
   
### def BotStart():
The "BotStart" method is responsible for starting the Messenger bot. First, it obtains the message input element and the last message sent by the target user. Then, it enters a loop that waits for new messages from the user and responds to them. If the last message is the same as the one previously ignored, the loop continues without responding. To generate a response, it uses the "Question(msg:str)" method from the "ChatBot" class. If a valid response is obtained, it sends it back to the user.

### def GetMessager(user_type):
This method, named "GetMessager", is used to obtain messages from the target user or author. It raises a ValueError if the UserType parameter is not a string or an Exception if an invalid parameter is passed. It uses a dictionary to map the UserType string to the corresponding CSS selector name used by Messanger to identify messages from the desired user. The method then obtains messages from the desired user and returns them as a list of strings.
| Parameter   | type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_type`| `string` | **Mandatory**.  Type of user to obtain messages from ("author" or "user").|

|Return| type       | Description                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | list of strings containing the message of the user_type specified.|

