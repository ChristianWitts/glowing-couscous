pub fn hello(name: Option<&str>) -> String {
    if name.is_some() {
        format!("Hello, {}!", name.unwrap().to_string())
    } else {
        "Hello, World!".to_string()
    }
}
