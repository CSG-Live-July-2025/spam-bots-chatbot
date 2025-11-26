require "dotenv/load"
require "openai"
require "net/http"

# =============================================================================
# RUBY VERSION 2: Using OpenAI SDK (Requires Patch)
# =============================================================================
# Pros: Uses official SDK, simpler API calls
# Cons: Need complex patch (19 lines) to fix macOS SSL issue
# =============================================================================

# macOS SSL fix - Use Net::HTTP to handle certificate verification
# This is needed because the OpenAI gem creates connections before we can
# configure them, and macOS OpenSSL 3.x has strict CRL checking
module Net
  class HTTP
    alias_method :original_use_ssl=, :use_ssl=
    
    def use_ssl=(flag)
      self.original_use_ssl = flag
      if flag && !@cert_store
        self.verify_mode = OpenSSL::SSL::VERIFY_PEER
        self.cert_store = OpenSSL::X509::Store.new
        self.cert_store.set_default_paths
        # By not setting CRL check flags, we avoid the macOS SSL error
      end
    end
  end
end

# =============================================================================
# Now we can use the OpenAI SDK normally
# =============================================================================

client = OpenAI::Client.new

assistant_message = "I'm a chatbot! Ask me anything:"
puts "Assistant: #{assistant_message}\n\n"

print "User: "
user_input = gets.chomp

messages = [
  { role: "system", content: "You are a helpful AI assistant." },
  { role: "assistant", content: assistant_message },
  { role: "user", content: user_input }
]

while user_input != "exit"
  # Using the OpenAI SDK's responses.create method
  response = client.responses.create(
    model: "gpt-4o-mini",
    input: messages,
    temperature: 0
  )
  
  # Extract response from the SDK response object
  assistant_response = response[:output][0][:content][0][:text]
  puts "\nAssistant: #{assistant_response}"
  
  print "\nUser: "
  user_input = gets.chomp
  
  messages << { role: "assistant", content: assistant_response }
  messages << { role: "user", content: user_input }
end

puts "\nGoodbye!"
