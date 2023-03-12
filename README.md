<div align="center"><h1><b>Collab🤝Land Actions FastAPI Template</b></h1></div>

## **Introduction** 🙏

The repository serves as a FastAPI template for implementing Collab.Land actions for Discord interactions. The Collab.Land actions are installed to the Collab.Land bot through the **`/test-flight`** miniapp available in the Collab.Land marketplace.

## **Pre-requisites** 💻

### Environment:

- Python 3.8.5 [[Download Here](https://www.python.org/downloads/)]
- Poetry 1.4.0 [[Instructions to Download](https://python-poetry.org/docs/)]

### Tunnel Forwarding:

- NGROK [[Installation Instructions](https://ngrok.com/docs/getting-started)]

## **Server Setup** ⚙️

### Starting the server:

- Clone the repository to your machine
- Open the folder in a code editor of your choice
- Install dependencies:
  ```bash
  poetry install
  ```
- Set the PORT variable in the `.env` file:
  ```bash
  echo "PORT=8000" >> .env
  ```
- Start the server:

  ```bash
  poetry run start
  ```

- To expose your localhost API to public domain, open a new terminal and start NGROK:
  ```bash
  ngrok http <PORT>
  ```
- Copy the `.ngrok.io` link shown in your terminal

### Installing the Collab.Land actions:

- The API exposes 3 types of Collab.Land actions:
  - `<NGROK URL>/hello-action` : Sample Discord interaction demo-ing Discord message interactions
  - `<NGROK URL>/button-action` : Sample Discord interaction demo-ing Discord button interactions
  - `<NGROK URL>/popup-action` : Sample Discord interaction demo-ing Discord modal interactions
- Use the `/test-flight install action-url: <Your action URL>` command in the Collab.Land Bot to install the Collab.Land actions.

## **API Specifications** 🛠️

- The API exposes two routes per slash command:
  - GET `/hello-action/metadata` : To provide the metadata for the `/hello-action` command
  - POST `/hello-action/interactions` : To handle the Discord interactions corresponding to the `/hello-action` command
  - GET `/button-action/metadata` : To provide the metadata for the `/button-action` command
  - POST `/button-action/interactions` : To handle the Discord interactions corresponding to the `/button-action` command
  - GET `/popup-action/metadata` : To provide the metadata for the `/popup-action` command
  - POST `/popup-action/interactions` : To handle the Discord interactions corresponding to the `/popup-action` command
- The slash commands provide example codes for the following Discord interactions:
  - `/hello-action` : It shows how to interact with a basic slash command Discord interaction, and then reply to that interaction. Along with that it shows an example of how to edit messages, delete messages or send follow-up messages using Collab.Land actions.
  - `/button-action` : It shows how to create buttons using Discord interactions, and then respond to the button events.
  - `/popup-action` : It shows how to send modals for forms using Discord interactions, and then listen for the form submissions and even read data submitted by the user.

## **Contributing** 🫶

- Please go through the following article [[**Link**](https://dev.collab.land/docs/upstream-integrations/build-a-custom-action)] to understand the deep technical details regarding building on the Collab.Land actions platform.
- In order to change the slash commands for the actions, try editing the `Metadata` models mentioned in the metadata route handlers [[Here 👀]](collabland_action_fastapi/hello_action/main.py#L21)
- In order to change the logic which runs on the slash commands, try changing the `post_hello_action_interaction()` function mentioned in the `hello-action` interaction route handler [[Here 👀]](collabland_action_fastapi/hello_action/main.py#L58)

---

<div align="center"><b><i><small>Built with ❤️ and 🤝 by Collab.Land</small></i></b></div>
