package main

import (
    "log"
    "time"
    "gopkg.in/mgo.v2"
    // "gopkg.in/mgo.v2/bson"
)

type User struct {
    UserID string
    Nickname string
    lastMessage string
    Timestamp time.Time
}

func newUser(UserName string) User {
    var currUser User
    currUser.UserID = UserName
    currUser.Nickname = ""
    currUser.lastMessage = ""
    currUser.Timestamp = -1

    return currUser
}

var (
    MongoSession *mgo.Session
    UsersCollection *mgo.Collection
)

func initializeDataBase() {
    MongoSession, err := mgo.Dial("127.0.0.1")
    if err != nil {
        panic(err)
    }

    defer MongoSession.close()

    MongoSession.SetMode(mgo.Monotonic, true)

    UsersCollection := session.DB("main").C("people")
}

func updateUserDatabase(user User) bool {
    user.Timestamp = time.now
    // Ensure that the user doesn't already exist
    // ifExist := UsersCollection.Find(bson.M{"_"})
    err := UsersCollection.Insert(user)

    if err != nil {
        log.Fatal(err)
        return false
    }
    return true
}

func getUserInformation(UserName string) User {
    return newUser("hello")
}
