pub type Solution<T> = fn(&String) -> T;
pub type DaySol = (Solution<String>, Solution<String>);
