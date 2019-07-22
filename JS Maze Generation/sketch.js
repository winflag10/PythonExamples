var cols, rows;// done apart from drawing a red line from start to finish and optimishing to check when solved rsther than looping width times
var w = 50; //width and height of each square
var grid = [];
var current;
var stack = [];
var done = false;
var solved = false;
var deadEndFilled = false;
var changes = 0;
var deadEnds = [];
var restarted = 0;

function index(i,j){
  if (i<0 || j<0 || i > cols-1 || j > rows - 1){
    return undefined;
  }
  return i + (j * cols);
}
function setup() {
	createCanvas(500,500);
	cols = floor(width/w);
	rows = floor(height/w);
	frameRate(60);
	for (var j = 0; j < rows; j++) {
		for (var i = 0; i < cols; i++){
				var cell = new Cell(i,j);
			  grid.push(cell);
		}
	}

	current = grid[0];
	current.visited = true;
}
function draw() {
	background(51);
	for (var i = 0; i < grid.length; i++){
		grid[i].show();
	}
	if (!done){
		genMaze()
	}else if (!solved){
		solveMaze()
  }
}
function genMaze(){
	var next = current.checkNeighbors();
	if (next){
		stack.push(next);
		next.visited = true;//set next cell as visited
		removeWalls(current,next);
		current.current = false;//set the cell you are moving from as not current
		current = next;//set the next cell as the current cell
		current.current = true;//mark the new cell as the current cell
	}else if (stack.length > 0) {
		var cell = stack.pop();
		current = cell
		current.current = false;
	}else{
		done = true;
	};
}
function removeWalls(current,next){
	var x = current.i - next.i;
	if (x === 1) {
		current.sides[3] = false;
		next.sides[1] = false;
	}else if (x === -1) {
		current.sides[1] = false;
	  next.sides[3] = false;
	}
	var y = current.j - next.j;
	if (y === 1) {
		current.sides[0] = false;
		next.sides[2] = false;
	}else if (y === -1) {
		current.sides[2] = false;
	  next.sides[0] = false;
	}
}


function isJunction(abcd){
	if (abcd){
		if (abcd.sideCount() == 1){
      //console.log("junction at ",index(abcd.i,abcd.j))
			return true;
		}else{
      return false
    }
	}
}

//
// //first attempt at solving the grid using Dead end filling. didnt work, but does now! :D
function solveMaze(){
  if(!deadEndFilled){
  	for (var i = 1; i < grid.length-1; i++){
  		var counter = grid[i].sideCount()
  		if (counter == 3){//if dead end
  			grid[i].blocked = true;//fills red
        //console.log("dead end at",index(grid[i].i,grid[i].j))

        deadEnds.push(grid[i])

  		}
  	}
  }
  deadEndFilled = true;
  //console.log(deadEnds.length)
  if(deadEnds.length != 0){
    fillToJunction()
  }
}


function fillToJunction(){
  //console.log("here")
  if (deadEnds.length != 0){//if there are still dead ends
    deadEnd = deadEnds.pop();
    //console.log("got new dead end",index(deadEnd.i,deadEnd.j))
    next = deadEnd.checkNeighborsJunction();//finds next cell to fil
    if(next){
      //console.log("next would be",index(next.i,next.j))
      if(!isJunction(next)){//if the cell isnt a junction
        next.blocked = true;
        //console.log("blocked",index(next.i,next.j))
        deadEnds.push(next);
        //console.log("added ",index(next.i,next.j)," to deadends")
      }
    }
  }
  if (restarted <= rows){
    if (deadEnds.length == 0){//if there are no more dead ends
      //console.log("restarted")
      for (var i = 1; i < grid.length-1; i++){
    		var counter = grid[i].sideCountIncBlocked()
    		if (counter == 3){//if dead end
    			grid[i].blocked = true;//fills red
          //console.log("dead end at",index(grid[i].i,grid[i].j))

          deadEnds.push(grid[i])

    		}
    	}
    restarted++
    }
  }else if(restarted > rows){
    for (var i = 1; i < grid.length-1; i++){
      if (!grid[i].blocked){
        grid[i].path = true;
      }
    }
  }
}














//whitespace
