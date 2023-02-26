// http://mb0f0g.ctf.cc-sw.com/
// curl -d $'user=a' -X POST http://mb0f0g.ctf.cc-sw.com/login
package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/hex"
	"encoding/json"
	"fmt"
)

type UserInfo struct {
	Name string `json:"user"`
	Role string `json:"role"`
}

var AppSecretKey []byte
var Flag []byte

func main() {
	AppSecretKey := []byte("Here is a string")

	user := UserInfo{Name: "\n\n\n", Role: "users"}
	token, _ := json.Marshal(&user)
	fmt.Println(string(token[:]))

	sessionID, _ := encryptToken(AppSecretKey, token)

	result := hex.EncodeToString(sessionID)
	fmt.Println(result)

	jsontext := []byte("{\"role\":\"a\",\"ole\":\"users\"}")
	var unmar UserInfo
	json.Unmarshal(jsontext, &unmar)
	//fmt.Println(unmar.Role)

}

// CRYPTO
func pkcs7Pad(message []byte) []byte {
	padVal := aes.BlockSize - (len(message) % aes.BlockSize)
	padding := []byte{byte(padVal)}
	return append(message, bytes.Repeat(padding, padVal)...)
}

func pkcs7Unpad(message []byte) []byte {
	if message == nil || (len(message)%16) != 0 {
		return nil
	}

	padVal := message[len(message)-1]
	if padVal > 16 {
		return nil
	}

	padRange := len(message) - int(padVal)
	if padRange <= 0 {
		return nil
	}

	for _, pad := range message[padRange:] {
		if pad != padVal {
			return nil
		}
	}

	return message[:padRange]
}

func encryptToken(key []byte, userInfo []byte) ([]byte, error) {
	var aesCipher cipher.Block

	iv := []byte("0000000000000000") //make([]byte, aes.BlockSize)
	var err error
	//_, err := rand.Read(iv)
	// if err != nil {
	// 	return nil, errors.New("Encrypt failed")
	// }

	plaintext := pkcs7Pad([]byte(userInfo))

	fmt.Println(hex.EncodeToString(plaintext))

	token := make([]byte, len(iv)+len(plaintext))
	if aesCipher, err = aes.NewCipher(key); err != nil {
		return nil, err
	}

	copy(token[:aes.BlockSize], iv)
	encrypter := cipher.NewCBCEncrypter(aesCipher, iv)
	encrypter.CryptBlocks(token[aes.BlockSize:], plaintext)

	return token, nil
}

func decryptToken(key []byte, token []byte) []byte {
	var aesCipher cipher.Block
	var err error

	if aesCipher, err = aes.NewCipher(key); err != nil {
		return nil
	}

	iv := token[:aes.BlockSize]
	userInfo := make([]byte, len(token)-aes.BlockSize)

	decrypter := cipher.NewCBCDecrypter(aesCipher, iv)
	decrypter.CryptBlocks(userInfo, token[aes.BlockSize:])

	return pkcs7Unpad(userInfo)
}
