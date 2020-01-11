import base64
import os
from pathlib import Path

homePath = os.getenv('HOME') + '/'
KDEEmojiProcessingPath = 'KDEEmojiProcessing/'
KDEEmoticonsBasePath = '.local/share/emoticons/'
iOS = 'iOS/'

def read_file():
    """Reads the Unicode's HTML page content, splitting it into a array sorted by Emoji."""
    print('Reading file...')

    data = []
    with open(homePath + KDEEmojiProcessingPath + 'unicodeEmojis.html') as file:
        data = file.read().replace('\n', '')
        data = data.split('<td class="rchars">')
        data.remove(data[0])
    
    print('OK.')
    return data

def getNamesAndHashes(dataByEmoji):
    """Based on the received HTML Data, this function will compose an array of tuples containing Emoji Data.
    The tuples are organized like: (Emoji Name, Emoji Base64 Hash)"""
    print('Splitting HTML data by emoji...')

    namesAndHashes = []

    for item in dataByEmoji:
        tempHashes = item.split('src="')
        emojiHash = tempHashes[1].split('"')
        emojiHash = emojiHash[0][22:]

        tempNames = item.split('class="name">')
        tempNames = tempNames[1].split('</td>')
        emojiName = tempNames[0]

        emojiTuple = emojiName, emojiHash
        namesAndHashes.append(emojiTuple)

    print('OK.')
    return namesAndHashes

def decodeBase64ImagesWithName(namesAndHashes):
    """Decodes and creates a PNG Image with Emoji name and its Base64 hash saving it into KDE's default emoticon path"""
    print('Decoding and creating PNGs by hashes...')
    for nameAndHash in namesAndHashes:
        emojiName = nameAndHash[0]
        emojiByteConvertedHash = bytearray(nameAndHash[1], 'utf-8')

        Path(homePath + KDEEmoticonsBasePath + iOS).mkdir(parents=True, exist_ok=True)

        with open(homePath + KDEEmoticonsBasePath + iOS + emojiName + '.png', 'wb') as processableImage:
            processableImage.write(base64.decodebytes(emojiByteConvertedHash))

    print('OK.')

def replaceOnKDEsXML(namesAndHashes):
    """Populates the KDE's XML with correct image names, based on the empty XML"""
    print('Creating KDE-friendly XML for the Emojis...')

    KDEFile = open(homePath + KDEEmojiProcessingPath + 'emoticonsBaseStrings.xml', 'r')

    data = KDEFile.read()
    manageableData = data.split('<messaging-emoticon-map>')
    manageableData = manageableData[1].split('</emoticon>')
    manageableData.pop()

    for i, data in enumerate(manageableData):
        manageableData[i] = manageableData[i].replace('file=""', 'file="' + namesAndHashes[i][0] + '.png"')
        manageableData[i] = manageableData[i] + '</emoticon>'

    finalData = '<?xml version=\'1.0\'?>\n<messaging-emoticon-map>'
    for emoticon in manageableData:
        finalData = finalData + emoticon
    finalData = finalData + '\n</messaging-emoticon-map>'

    KDENewFile = open(homePath + KDEEmoticonsBasePath + iOS + 'emoticons.xml', 'w')
    KDENewFile.write(finalData)
    
    print('OK.')




if __name__ == "__main__":
    dividedByEmoji = read_file()
    namesAndHashes = getNamesAndHashes(dividedByEmoji)
    decodeBase64ImagesWithName(namesAndHashes)
    replaceOnKDEsXML(namesAndHashes)
    
    print('Finished Emoji processing.')


