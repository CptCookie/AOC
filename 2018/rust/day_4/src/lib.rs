enum Guard_state {
    WakeUp,
    Awake,
    FallAsleap,
    Sleep
}
struct Date {
    day: u32,
    month: u32,
}

struct Shift {
    date: Date,
    awake: Vec<Guard_state>
}

struct Guard {
    id: i32,
    shifts: Vec<Shift>
}

struct Guard_Squad {
    squad: Vec<Guard>
}

impl Guard_Squad {
    fn get_guard_or_create(&mut self, id: &i32) -> &mut Guard {
        let mut search_guard: Option<&mut Guard> = None;
        {
            search_guard = self._get_guard(id);
        }
        match search_guard {
            Some(n) => return n,
            None => {
                let mut guard = Guard::new(id);
                self.squad.push(guard);
                return self._get_guard(id).unwrap()
            }
        };
    }

    fn _in_squad(&self, id: &i32) -> bool{
        self.squad.iter().any(|n| n.id == *id)
    }

    fn _get_guard(&mut self, id: &i32) -> Option<&mut Guard>{
        for n in self.squad.iter_mut() {
            if n.id == *id {
                return Some(n);
            }
        }
        None
    }

}

impl Guard {
    fn add_shift(&mut self, shift: Shift) {
        self.shifts.push(shift)
    }

    fn new(n: &i32) -> Guard{
        let id = *n;
        Guard{id, shifts:vec![]}
    }
}

impl Shift{
    fn new(date: Date) -> Shift{
        let awake: Vec<Guard_state> = Vec::with_capacity(120); // starting 23:30 ending 0:29

        Shift{awake, date}
    }

    fn set_shift() {

    }
}

