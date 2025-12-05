use proc_macro::TokenStream;
use proc_macro2;
use quote::quote;
use syn::{parse_macro_input, punctuated::Punctuated, DeriveInput, Expr, Token};

#[proc_macro_attribute]
pub fn mark_solution(attr: TokenStream, item: TokenStream) -> TokenStream {
    let args = parse_macro_input!(attr with Punctuated::<Expr, Token![,]>::parse_terminated);

    if args.len() != 2 {
        return syn::Error::new(
            proc_macro2::Span::call_site(),
            "Expected exactly 2 arguments: year and day",
        )
        .to_compile_error()
        .into();
    }

    let year = &args[0];
    let day = &args[1];

    let input = parse_macro_input!(item as DeriveInput);
    let struct_name = &input.ident;

    // Use absolute paths to avoid naming conflicts
    let expanded = quote! {
        #input

        ::inventory::submit! {
            crate::SolutionEntry {
                year: #year,
                day: #day,
                factory: || ::std::boxed::Box::new(#struct_name),
            }
        }
    };

    TokenStream::from(expanded)
}
