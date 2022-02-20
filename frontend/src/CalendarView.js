import Kalend, { CalendarView } from 'kalend' // import component
import 'kalend/dist/styles/index.css'; // import styles

function CAL({viewEvents}) {
    return(
        <div  style={{
            height: '100vh'
          }}>
    <Kalend
    //   onEventClick={onEventClick}
    //   onNewEventClick={onNewEventClick}
    events={
        viewEvents
    }
    initialDate={new Date().toISOString()}
       hourHeight={60}
      initialView={CalendarView.WEEK}
       disabledViews={[CalendarView.DAY]}
    //   onSelectView={onSelectView}
    //   selectedView={selectedView}
    //   onPageChange={onPageChange}
       timeFormat={'24'}
      weekDayStart={'Monday'}
    //   calendarIDsHidden={['work']}
    //   language={'en'}
    />
    </div>
    )
}
    export default CAL;