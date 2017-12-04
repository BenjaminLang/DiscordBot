package main

import (
    "encoding/json"
    "fmt"
    "os"
    "io/ioutil"
)

type Key struct {
    Token string `json:"token"`
}

func getToken() Key {
    jsonFile, err := os.Open("token.json")

    if err != nil {
        fmt.Println(err.Error())
        os.Exit(1)
    }

    defer jsonFile.Close()

    byteValue, _ := ioutil.ReadAll(jsonFile)

    var botKey Key
    json.Unmarshal(byteValue, &botKey)
    return botKey
}

func (inputKey Key) toString() string {
    return inputKey.Token
}
