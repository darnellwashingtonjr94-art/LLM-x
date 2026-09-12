pub struct MPTCP SocketSplicer {
    pub pool_active: bool,
    pub path_striping_factor: u8,
}

impl MPTCP SocketSplicer {
    pub fn new(factor: u8) -> Self {
        Self {
            pool_active: true,
            path_striping_factor: factor,
        }
    }

    pub fn splice_sockets(&self) -> String {
        format!("MPTCP/QUIC path bonding active with striping factor: {}", self.path_striping_factor)
    }
}
