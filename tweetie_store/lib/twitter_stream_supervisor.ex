defmodule TwitterStreamSupervisor do
  
  def start(_type, _args) do
    import Supervisor.Spec

    workers = [
      worker(TwitterStream, []),
      worker(TwitterStreamConsumer, ["#заСлободенСофтвер"], id: 1),
    ]

    Supervisor.start_link(workers, strategy: :one_for_one)
  end
  
end
