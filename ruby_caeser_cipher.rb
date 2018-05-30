def encrypt(message, shift)
    # 97-122

    encrypted_message = ""

    message.split("").each do |letter|

      if letter == " "
        encrypted_message += " "
      else
        if letter.ord + shift > 122
          index = (letter.ord + shift) - 26
          encrypted_message += index.chr
        else
          index = letter.ord + shift
          encrypted_message += index.chr
        end
      end

    end

    puts encrypted_message
  end

encrypt("This is my secret message", 2)
