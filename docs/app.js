/* my own custom js html injector to avoid pasting the same page over and over */
const regex = /<body[^>]*>((.|[\n\r])*)<\/body>/im;
//set of all pages
const pages = {
  0: "intro.html",
  1: "plan.html",
  2: "design.html",
  3: "create.html",
  4: "evaluate.html",
  5: "reflection.html"
}

let current_page = 0;

//function that loads active page into "inject" div
async function load_html() {
  const response = await fetch(`pages/${pages[current_page]}`);
  const text = (await response.text()).match(regex);
  document.getElementById("inject").innerHTML = text[0];
}

//function that swaps to next page
async function next_page() {
  if (current_page == 5) {
    current_page = 0;
  } else {
    current_page++;
  }
  load_html();
}

//function that loads specified page
async function goto_page(page) {
  current_page = page;
  load_html();
}

//heading highlight function
async function heading_click(page, heading_order) {
  goto_page(page);
  if (heading_order == 1) {
    document.getElementsByClassName("h3-1").style.backgroundColor = "#73C2FB";
  } else if (heading_order == 2) {

  } else if (heading_order == 3) {

  }
}

//initial load call to display content
load_html();
