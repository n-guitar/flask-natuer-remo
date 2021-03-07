
// select manu controller
const select_products = document.querySelectorAll(".list");
const click_or_ontouch = window.ontouchstart ? 'touchstart' : 'click';
console.log(click_or_ontouch)

select_products.forEach((el, i) => {
    el.addEventListener(click_or_ontouch, () => {
        selected = el.getAttribute("select-filter");
        el.classList.add("active");

        // Delete active class for the button that was pressed.
        select_products.forEach((v, k) => {
            if (i == k) {
                //pass
                ;
            } else {
                select_products[k].classList.remove("active");
                console.log("info:remove active class:");
            }
        });
        // Inactive all button. remove active class.
        const select_btns = document.querySelectorAll(".btnBox");
        select_btns.forEach((v, k) => {
            select_btns[k].classList.remove("active");
            console.log("info:.btnBox all remove active class:");
        });
        // Activate the button corresponding to the button you pressed.
        const active_btn = ".btnBox." + selected;
        const active_btns = document.querySelectorAll(active_btn);
        active_btns.forEach((v, k) => {
            active_btns[k].classList.add("active");
            console.log("info:select .btnBox add active class:");
        });
    });
});

// sending anime controller
const sending_anime = (status) => {
    const sendingwrap = document.querySelector("#sendingWrap");
    if (status == "sending") {
        sendingwrap.classList.add("active");
    } else if(status == "done") {
        sendingwrap.classList.remove("active");
    }
};

// send api
const signal_fetch = async (url, appliance_id, signal) => {
    sending_anime("sending");
    if (url.match(/other/)) {
        // other appliance
        signal_id = signal
        fetch_url = url + "/" + signal_id;
    } else {
        // tv air appliance
        fetch_url = url + "/" + appliance_id + "/" + signal;
    }
    await fetch(fetch_url, {
        method: "POST",
    })
        .then((response) => response.text())
        .then((text) => {
            console.log(text);
            sending_anime("done");
        });
};

// click button action
const click_btn_action = (target_btn_class_name, action_url) => {
    let action_btn = document.querySelectorAll(target_btn_class_name);
    action_btn.forEach((el, i) => {
        el.addEventListener(click_or_ontouch, () => {
            appliance_id = document
                .querySelector(".list.active")
                .getAttribute("select-filter");
            appliance_id = appliance_id.slice(3);
            signal = el.querySelector(".signal").id;
            // other appliance
            if (target_btn_class_name.match(/other/)) {
                signal = signal.slice(3);
            }
            console.log("click:", appliance_id, signal);
            signal_fetch(
                (url = action_url),
                (appliance_id = appliance_id),
                (signal = signal)
            );
        });
    });
};

// click button action instance
// air
click_btn_action(target_btn_class_name=".power > .airbtn",action_url="/air/api/send/power")
click_btn_action(target_btn_class_name=".mode > .airbtn",action_url="/air/api/send/mode")
click_btn_action(target_btn_class_name=".vol > .airbtn",action_url="/air/api/send/vol")
click_btn_action(target_btn_class_name=".dir > .airbtn",action_url="/air/api/send/dir")
// tv
click_btn_action(target_btn_class_name=".btnBox.tv",action_url="/tv/api/send")
// other
click_btn_action(target_btn_class_name=".btnBox.other",action_url="/other/api/send_signal")


const air_temp_btns = document.querySelectorAll(".temperature > .airbtn");
air_temp_btns.forEach((el, i) => {
    // console.log(el);
    el.addEventListener(click_or_ontouch, (e) => {
        appliance_id = document
            .querySelector(".list.active")
            .getAttribute("select-filter");
        appliance_id = appliance_id.slice(3);
        signal = el.querySelector(".signal").id;
        temp_num_aria = document.querySelector(
            ".temperature > .airbtn > .signal"
        );
        temp_num = temp_num_aria.innerText;
        if (signal == "temp-up") {
            if (Number(temp_num) < 30.0) {
                temp_num = Number(temp_num) + 0.5;
                temp_num_aria.textContent = temp_num;
            }
        } else if (signal == "temp-down") {
            if (Number(temp_num) > 18.0) {
                temp_num = Number(temp_num) - 0.5;
                temp_num_aria.textContent = temp_num;
            }
        }
        console.log("click:", appliance_id, signal, temp_num);
        signal_fetch(
            (url = "/air/api/send/temp"),
            (appliance_id = appliance_id),
            (signal = temp_num)
        );
    });
});