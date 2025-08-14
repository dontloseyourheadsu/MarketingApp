use leptos::prelude::*;

#[component]
pub fn AdvertisementsDashboard() -> impl IntoView {
    view! {
        <div class="page advertisements-dashboard">
            <h1 class="page-title">"Advertisements Dashboard"</h1>
            
            <div class="filters-section">
                <div class="filters-placeholder">
                    "Filters"
                </div>
            </div>

            <div class="content-section">
                <div class="content-placeholder">
                    "Content"
                </div>
            </div>
        </div>
    }
}
