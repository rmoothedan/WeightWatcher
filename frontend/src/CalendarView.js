import Kalend, { CalendarView } from 'kalend' // import component
import 'kalend/dist/styles/index.css'; // import styles

function CAL() {
    return(
        <div  style={{
            height: '100vh'
          }}>
    <Kalend
    //   onEventClick={onEventClick}
    //   onNewEventClick={onNewEventClick}
    events={
        {
            id: 1,
            startAt: '2022-02-19T18:03:00.000Z',
            endAt: '2022-02-19T19:04:00.000Z',
            summary: 'test',
            color: 'blue',
            calendarID: 'Calendar'
        }
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