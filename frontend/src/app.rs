use leptos::prelude::*;

use crate::nav_bar::NavigationBar;
use crate::pages::AdvertisementsDashboard;

#[component]
pub fn App() -> impl IntoView {
    let (is_collapsed, set_collapsed) = signal(false);

    view! {
        <div class="app-container">
            <NavigationBar is_collapsed=is_collapsed set_collapsed=set_collapsed />
            
            <main class=move || format!("main-content {}", if is_collapsed.get() { "sidebar-collapsed" } else { "" })>
                <AdvertisementsDashboard />
            </main>
        </div>
    }
}
