import datetime
import streamlit as st

def date_filter(min_date, max_date):
    today_date = datetime.date.today()
    allowed_max_date = max(max_date, today_date)

    with st.container(border=True, key="date_card_container"):
        st.markdown(
            '<div class="top-bar-label">Filter Date</div>',
            unsafe_allow_html=True,
        )
        date_range = st.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=allowed_max_date,
            label_visibility="collapsed",
            key="date_range_picker",
        )
        if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
            start_date, end_date = date_range
        else:
            start_date = (
                date_range[0]
                if isinstance(date_range, (tuple, list)) and len(date_range) > 0
                else min_date
            )
            end_date = max_date

    return start_date, end_date
