defmodule TwitterStreamConsumer do
  use GenStage

  def start_link(hashtag) do
    GenStage.start_link(TwitterStreamConsumer, hashtag)
  end

  def init(hashtag) do
    {:consumer, hashtag, subscribe_to: [TwitterStream]}
  end
  
  def handle_events(events, _from, state) do
    IO.inspect events
    IO.inspect state
  end

end
