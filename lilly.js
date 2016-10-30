window.onload = function()
{

var write_here = document.getElementById('write_here');
var dob_day = document.getElementById('dob-day');
}
function doThis() {
      write_here.innerHTML = dob_day.options[dob_day.selectedIndex].value;
}    



<div style="height:50px;width:300px;background-color:pink;">
      <p id="write_here"></p>
</div>

</div>

<script>
var write_here = document.getElementById('write_here');
var dob_day = document.getElementById('dob-day');

function doThis() {
      write_here.innerHTML = dob_day.options[dob_day.selectedIndex].value;
}      

</script>
