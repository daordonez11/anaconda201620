export const request = (state=[], action) => {
  switch (action.type) {
    case 'ADD_REQUEST':
      let newRequest = Object.assign({}, action.data, {
        id: +new Date
      });
      return state.concat([newRequest]);
      break;
    default:
      return state ;
  }
};

const modalDefault = {show: false,type: "error", title: "",text: ""};
export const saModal = (state=modalDefault, action) => {
  let ma = {};
  switch (action.type) {
    case 'HIDE_SA_MODALS':
       ma = Object.assign(state, action.data, {
        show: false
      });
      return  ma || state;
      break;
    case 'SHOW_SA_MODALS':
      ma = Object.assign({}, action.data);
      return  ma || state;
      break;
    default:
      return state ;
  }
};

const soundtrackDefault = {"sounds":
      [{ id: 1, sound: "", type: "", artist: "", rating: 0, likes: "" }]
};
export const soundtracks = (state=soundtrackDefault,  action) => {
  switch (action.type) {
    case 'GET_SOUNDTRACKS':
      return action.data || state;
      break;
    default:
      return state ;
  }
};
const notificationsDefault = {"notifications":
  [{ id: 0, name: "", notification_type: "", initial_date: "", closing_date: "", description: "" }
]};
export const notifications = (state=notificationsDefault,  action) => {
  switch (action.type) {
    case 'GET_NOTIFICATIONS':
      return action.data || state;
      break;
    default:
      return state ;
  }
};
