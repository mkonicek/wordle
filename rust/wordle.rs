use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;

fn load_words() -> Vec<String> {
  let file_content = fs::read_to_string("../words.txt")
    .expect("Something went wrong reading the file");
  return file_content.lines().map(str::to_string).collect();
}

fn character_frequencies(words: Vec<String>) -> HashMap<char, i64> {
  let mut freq = HashMap::new();
  for word in words {
    for c in word.chars() {
      *freq.entry(c).or_insert(0) += 1;
    }
  }
  freq
}

fn main() {
    let words = load_words();
    let freq = character_frequencies(words);
    let mut initial_allowed_set: HashSet<char> = HashSet::new();
    for c in freq.keys() {
      initial_allowed_set.insert(*c);
    }
    let mut allowed = vec![initial_allowed_set.clone(), initial_allowed_set.clone()];
    allowed[1] = vec!['c'].into_iter().collect();
    println!("freq {:?}", freq);
    println!("allowed {:?}", allowed);
}
