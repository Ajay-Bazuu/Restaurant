// var tablinks =document.getElementsByClassName("tab-link");
// var tabcontents =document.getElementsByClassName("tab-content");

// function opentab(tabname){
//     for(tablink of tablinks){
//         tablink.classList.remove("active-link");
//     }

//     for(tabcontent of tabcontents){
//         tabcontent.classList.remove("active-tab");
//     }
//     event.currentTarget.classList.add("active-link");
//     document.getElementById(tabname).classList.add("active-tab");
// }

function opentab(tabName) {
    // Remove active class from all tab links
    const tabs = document.querySelectorAll('.tab-links');
    tabs.forEach(tab => tab.classList.remove('active'));

    // Hide all tab contents
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.classList.remove('active-tab'));

    // Add active class to the clicked tab link
    const activeTab = document.querySelector(`.tab-links[onclick="opentab('${tabName}')"]`);
    if (activeTab) {
        activeTab.classList.add('active');
    }

    // Show the corresponding tab content
    const tabContent = document.getElementById(tabName);
    if (tabContent) {
        tabContent.classList.add('active-tab');
    }
}