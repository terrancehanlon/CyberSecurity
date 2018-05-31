require 'sinatra'
require 'sinatra/reloader'

get '/' do
  shift_value = params["shift"].to_i
  message = params["message"].to_s
  encrypted_message = encrypt(message, shift_value)
  erb :index, :locals => {:encrypted_message => encrypted_message}
end

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
    encrypted_message
  end

encrypt("This is my secret message", 2)
