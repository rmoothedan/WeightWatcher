import ApiCalendar from 'react-google-calendar-api';

function Calendar() {
    const handleClick = (event) => {
        ApiCalendar.handleAuthClick()
            .then(() => {
                console.log('we\'re in')
            })
            .catch((error) =>
            console.log(error)
            )
    }

    const getEvents = () => {
        if (ApiCalendar.sign)
            ApiCalendar.listEvents({
                timeMin: new Date().toISOString(),
                timeMax: new Date().addDays(10).toISOString(),
                showDeleted: true,
                maxResults: 10,
                orderBy: 'updated'
            }).then(({ result }: any) => {
                console.log(result.items);
            });
    }

    return (
        <div>
            <button
                onClick={(event) =>
                    handleClick(event)
                }
            >AUTH GOOGLE</button>
            { ApiCalendar.sign ? 
            <button
                onClick={() => {
                    getEvents() 
                }}>get 10 Events
            </button>
            : null
    }   
        </div>
    )
};

export default Calendar;