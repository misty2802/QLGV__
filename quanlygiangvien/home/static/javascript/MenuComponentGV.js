const ARRAY_MENU = [
    { id: 1, textMenu: "Diễn đàn", icon: '<i class="fa-solid fa-thumbs-up"></i>', to: "/forumad/", role: [0, 1] },
    { id: 3, textMenu: "Bài viết của tôi", icon: '<i class="fa-sharp fa-solid fa-mailbox"></i>', to: "/myforum/", role: [0,1] },
    { id: 4, textMenu: "Tài liệu", icon: '<i class="fa-solid fa-file"></i>', to: "./DocumentPage.html", role: [0, 1] },
    { id: 5, textMenu: "Về chúng tôi", icon: '<i class="fa-solid fa-user-tag"></i>', to: "./UsPage.html", role: [0, 1] }
];

function createMenu(user) {
    const filteredMenu = ARRAY_MENU.filter(menu => menu.role.includes(user.isRole));

    const menuContainer = document.createElement('div');
    menuContainer.className = 'menu_container';

    const bodyMenu = document.createElement('div');
    bodyMenu.className = 'body_menu';

    filteredMenu.forEach(menu => {
        const itemMenu = document.createElement('a');
        itemMenu.className = 'item_menu';
        itemMenu.href = menu.to;
        itemMenu.innerHTML = `${menu.icon} <div class="text_menu">${menu.textMenu}</div>`;
        bodyMenu.appendChild(itemMenu);
    });

    menuContainer.appendChild(bodyMenu);
    return menuContainer;
}

const user = { isRole: 0 }; 
document.getElementById('menuContainer').appendChild(createMenu(user));

