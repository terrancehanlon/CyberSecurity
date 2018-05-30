require 'sinatra'
require 'sinatra/reloader'

get '/' do
  number = rand(5)
  guess = params["guess"].to_i
  message = check_guess(guess, number)
  erb :index, :locals => {:number => number, :message => message}

end

def check_guess(guess, number)
  message = []
  if guess > number
    message = "too high"
  else
    message = "too low"
  end
  message
end
