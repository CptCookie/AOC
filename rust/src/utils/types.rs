pub type Solution<T> = fn(&String) -> T;
pub type Day<T> = Option(Solution<T>, Solution<T>);