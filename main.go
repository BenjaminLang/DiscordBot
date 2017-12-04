package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"github.com/bwmarrin/discordgo"
)

// Variables used for command line parameters
var (
	Token string
	Session *discordgo.Session
	Message *discordgo.MessageCreate
)

func init() {
    botToken := getToken()
    Token = botToken.toString()
}

func main() {
	// Create a new Discord session using the provided bot token.
	dg, err := discordgo.New("Bot " + Token)
	if err != nil {
		fmt.Println("error creating Discord session,", err)
		return
	}

	// Register the messageCreate func as a callback for MessageCreate events.
	dg.AddHandler(messageCreate)

	// Open a websocket connection to Discord and begin listening.
	err = dg.Open()
	if err != nil {
		fmt.Println("error opening connection,", err)
		return
	}

	// Wait here until CTRL-C or other term signal is received.
	fmt.Println("Bot is now running.  Press CTRL-C to exit.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
	<-sc

	// Cleanly close down the Discord session.
	dg.Close()
}

// This function will be called (due to AddHandler above) every time a new
// message is created on any channel that the autenticated bot has access to.
func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	Session = s;
	Message = m;
	// Ignore all messages created by the bot itself
	// This isn't required in this specific example but it's a good practice.
	if Message.Author.ID == Session.State.User.ID {
		return
	}

	switch Message.Content {
	case "ping":
		Session.ChannelMessageSend(Message.ChannelID, "Pong!")
		break
	case "pong":
		Session.ChannelMessageSend(Message.ChannelID, "Ping!")
		break
	case strings.HasPrefix(Message.content, "!history"):
		getHistory()
		break
	}
}

func storeMessage() {

}

func getHistory() {
	Session.ChannelMessageSend(Message.ChannelID, "Current History")
}
