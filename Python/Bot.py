def encrypt(text):
    #This is where the actual ROT13 is applied
    textlist = list(text)
    newtext = ''
    firsthalf = list('abcdefghijklmABCDEFGHIJKLM')
    lasthalf = list('nopqrstuvwxyzNOPQRSTUVWXYZ')
    for char in textlist:
        if char in firsthalf:
            newtext += lasthalf[firsthalf.index(char)]
        elif char in lasthalf:
            newtext += firsthalf[lasthalf.index(char)]
        else:
            newtext += char

    return newtext

class EncryptHandler(object):
    '''
    This bot allows users to quickly encrypt messages using ROT13 encryption.
    It encrypts/decrypts messages starting with @encrypt.
    '''

    def usage(self):
        return '''
            This bot uses ROT13 encryption for its purposes.
            It responds to me starting with @encrypt.
            Feeding encrypted messages into the bot decrypts them.
            '''

    def triage_message(self, message, client):

        original_content = message['content']

        # This makes sure that the bot only replies to messages it supposed to reply to.
        should_be_encrypted = original_content.startswith('@encrypt')

        return should_be_encrypted

    def handle_message(self, message, client, state_handler):
        original_content = message['content']
        temp_content = encrypt(original_content)
        new_content = "Encrypted/Decrypted text: " + temp_content                                               

        client.send_message(dict(
            type='stream',
            to=message['display_recipent'],
            subject=message['sender_email'] + "'s Encrpted text"
            content=new_content,
        ))

handler_class = EncryptHandler
