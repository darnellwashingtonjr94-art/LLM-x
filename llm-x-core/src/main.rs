mod orchestrator;
mod swarm;
mod network;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("[LLM-x] Initializing Sovereign Orchestrator Core...");
    orchestrator::router::init_router().await?;
    Ok(())
}
