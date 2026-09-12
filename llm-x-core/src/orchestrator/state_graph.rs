pub struct StateGraph {
    pub current_state: String,
    pub concurrency_limit: usize,
}

impl StateGraph {
    pub fn new(state: &str) -> Self {
        Self { current_state: state.to_string(), concurrency_limit: 10 }
    }
}
