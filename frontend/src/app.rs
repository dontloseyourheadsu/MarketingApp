use leptos::prelude::*;

use crate::nav_bar::NavigationBar;
use crate::pages::{AdsPage, AdvertisementsDashboard};

#[derive(Debug, Clone, PartialEq)]
pub enum CurrentPage {
    Advertisements,
    Ads,
    Metrics,
    Topics,
    Groups,
    OrgSettings,
}

#[component]
pub fn App() -> impl IntoView {
    let (is_collapsed, set_collapsed) = signal(false);
    let (current_page, set_current_page) = signal(CurrentPage::Advertisements);

    view! {
        <div class="app-container">
            <NavigationBar
                is_collapsed=is_collapsed
                set_collapsed=set_collapsed
                current_page=current_page
                set_current_page=set_current_page
            />

            <main class=move || format!("main-content {}", if is_collapsed.get() { "sidebar-collapsed" } else { "" })>
                {move || match current_page.get() {
                    CurrentPage::Advertisements => view! { <AdvertisementsDashboard /> }.into_any(),
                    CurrentPage::Ads => view! { <AdsPage /> }.into_any(),
                    CurrentPage::Metrics => view! { <div class="page"><h1>"Metrics Page"</h1></div> }.into_any(),
                    CurrentPage::Topics => view! { <div class="page"><h1>"Topics Page"</h1></div> }.into_any(),
                    CurrentPage::Groups => view! { <div class="page"><h1>"Groups Page"</h1></div> }.into_any(),
                    CurrentPage::OrgSettings => view! { <div class="page"><h1>"Organization Settings"</h1></div> }.into_any(),
                }}
            </main>
        </div>
    }
}
