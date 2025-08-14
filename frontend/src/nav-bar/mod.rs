use crate::app::CurrentPage;
use leptos::prelude::*;

#[component]
pub fn NavigationBar(
    #[prop(into)] is_collapsed: ReadSignal<bool>,
    #[prop(into)] set_collapsed: WriteSignal<bool>,
    #[prop(into)] current_page: ReadSignal<CurrentPage>,
    #[prop(into)] set_current_page: WriteSignal<CurrentPage>,
) -> impl IntoView {
    view! {
        <nav class=move || format!("sidebar {}", if is_collapsed.get() { "collapsed" } else { "" })>
            <div class="sidebar-header">
                <button
                    class="toggle-btn"
                    on:click=move |_| set_collapsed.set(!is_collapsed.get())
                >
                    {move || if is_collapsed.get() { "→" } else { "←" }}
                </button>
            </div>

            <div class="nav-content">
                <ul class="nav-menu">
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::Advertisements { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::Advertisements)
                    >
                        <span class="nav-label">"Advertisements"</span>
                    </li>
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::Metrics { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::Metrics)
                    >
                        <span class="nav-label">"Metrics"</span>
                    </li>
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::Ads { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::Ads)
                    >
                        <span class="nav-label">"Ads"</span>
                    </li>
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::Topics { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::Topics)
                    >
                        <span class="nav-label">"Topics"</span>
                    </li>
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::Groups { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::Groups)
                    >
                        <span class="nav-label">"Groups"</span>
                    </li>
                    <li
                        class=move || format!("nav-item {}",
                            if current_page.get() == CurrentPage::OrgSettings { "active" } else { "" })
                        on:click=move |_| set_current_page.set(CurrentPage::OrgSettings)
                    >
                        <span class="nav-label">"Org Settings"</span>
                    </li>
                </ul>
            </div>
        </nav>
    }
}
