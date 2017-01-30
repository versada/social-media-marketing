defmodule TwitterStream do
  use GenStage

  def start_link() do
    GenStage.start_link(TwitterStream, [])
  end

  def init(track) do
    stream = ExTwitter.stream_filter(track: "a") |> Stream.map(fn(tweet) -> tweet.text end)
    {:producer, stream}
  end

  def handle_demand(_, stream) do
    {:noreply, Enum.take(stream, 1), stream}
  end

end
