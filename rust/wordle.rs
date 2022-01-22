use std::fs;

fn load_words() -> Vec<String> {
  let file_content = fs::read_to_string("../words.txt")
    .expect("Something went wrong reading the file");
  return file_content.lines().map(str::to_string).collect();
}

fn main() {
    let words = load_words();
    println!("{:?}", words);
}