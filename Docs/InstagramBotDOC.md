## class InstagramBotGPT:
### def __init\__(user, chatbot):
Initializes the ChromeDriverManager service, creates a webdriver. Chrome instance, and navigates to the chat page of the provided Instagram username.
| Parameter   | type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user`| `string` | **Mandatory**. The Instagram username target to start a chat|
| `chatbot`| `object` | **Mandatory**. Instance of the ChatBot class.|
   
### def BotStart():
This method, named "BotStart", is responsible for starting the Instagram bot. Firstly, it obtains the message input element and the last message sent by the target user. Then, it enters a loop that waits for new messages from the user and responds to them. If the last message is the same as the one previously ignored, the loop continues without responding. To generate a response, it uses the "Question(msg:str)" method from the "ChatBot" class. If a valid response is obtained, it sends it back to the user.

### def GetMessager(user_type):
Method to obtain messages from the target user or author. Raises a ValueError if the UserType parameter is not a string or an Exception if an invalid parameter is passed. Uses a dictionary to map the UserType string to the corresponding CSS class name used by Instagram to identify messages from the desired user. Obtains messages from the desired user and returns them as a list of strings.
| Parameter   | type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_type`| `string` | **Mandatory**.  Type of user to obtain messages from ("author" or "user").|

|Return| type       | Description                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | list of strings containing the message of the user_type specified.|

